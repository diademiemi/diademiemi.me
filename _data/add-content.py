#!/usr/bin/env python3

import yaml
import argparse

STATUSES = {
    "1": "Maintained",
    "2": "Unmaintained",
    "3": "Deprecated"
}

def load_yaml(filename="ansible-content.yml"):
    with open(filename, 'r') as f:
        content = yaml.safe_load(f)
    return content

def save_yaml(data, filename="ansible-content.yml"):
    with open(filename, 'w') as f:
        yaml.safe_dump(data, f, default_flow_style=False)

def sort_content(content):
    # Sort the collections by name
    content['ansible_content']['collections'].sort(key=lambda x: x['name'].lower())

    # Sort roles within each collection
    for collection in content['ansible_content']['collections']:
        collection['roles'].sort(key=lambda x: x['name'].lower())

    # Also sort the standalone roles
    content['ansible_content']['roles'].sort(key=lambda x: x['name'].lower())

    return content

def add_new_role(content, role_name=None, ci=None, status=None):
    if not role_name:
        role_name = input("Enter the name of the role (e.g. diademiemi.discord or discord): ")
    if not status:
        status = prompt_for_status()
    has_ci = ci if type(ci) == bool else (input("Does the role have CI? (yes/no): ").lower() == "yes")

    author = content.get('default').get('author')
    if '.' not in role_name:
        role_name = f"{author}.{role_name}"

    role_repo_name = content['default']['role_repo_name'].format(name=role_name.split('.')[1])
    
    ci_badge = "" if not has_ci else content['default']['role_ci_badge_url'].format(git_url=content['default']['role_git_url'].format(author=author, role_repo_name=role_repo_name), name=role_name.split('.')[1])
    ci_url = "" if not has_ci else content['default']['role_ci_url'].format(git_url=content['default']['role_git_url'].format(author=author, role_repo_name=role_repo_name), name=role_name.split('.')[1])

    role = {
        "ci_badge": ci_badge,
        "ci_url": ci_url,
        "galaxy_url": content['default']['role_galaxy_url'].format(author=author, name=role_name.split('.')[1]),
        "gh_url": content['default']['role_git_url'].format(author=author, role_repo_name=role_repo_name),
        "name": role_name,
        "status": status
    }

    content['ansible_content']['roles'].append(role)

def interactive_mode(content):
    choice = input("Choose an option:\n1: Add a new role\n2: Add a new collection\n3: Add a new role to an existing collection\nEnter choice: ")
    
    if choice == "1":
        add_new_role(content)
    elif choice == "2":
        add_new_collection(content)
    elif choice == "3":
        role_name = input("Enter the name of the role you want to add: ")
        collection_name = input("Enter the name of the collection to which you want to add the role: ")
        add_role_to_collection(content, role_name, collection_name)

def add_new_collection(content, collection_name=None, status=None):
    if not status:
        status = prompt_for_status()

    if not collection_name:
        collection_name = input("Enter the name of the collection (e.g. diademiemi.vm_utils or vm_utils): ")

    author = content.get('default').get('author')
    if '.' not in collection_name:
        collection_name = f"{author}.{collection_name}"

    collection = {
        "galaxy_url": content['default']['collection_galaxy_url'].format(author=author, name=collection_name.split('.')[1]),
        "gh_url": content['default']['collection_git_url'].format(author=author, collection_repo_name=content['default']['collection_repo_name'].format(author=author, name=collection_name.split('.')[1])),
        "name": collection_name,
        "roles": [],
        "status": status  # This can be adjusted based on requirements
    }

    content['ansible_content']['collections'].append(collection)

def add_role_to_collection(content, role_name, collection_name, ci=None, status=None):
    if not status:
        status = prompt_for_status()
    has_ci = ci if ci is not None else (input("Does the role have CI? (yes/no): ").lower() == "yes")

    author = content.get('default').get('author')
    if '.' not in collection_name:
        collection_name = f"{author}.{collection_name}"
    if '.' not in role_name:
        role_name = f"{collection_name}.{role_name}"

    collection_repo_name = content['default']['collection_repo_name'].format(author=author, name=collection_name.split('.')[1])
    
    ci_badge = "" if not has_ci else content['default']['collection_role_ci_badge_url'].format(git_url=content['default']['collection_git_url'].format(author=author, collection_repo_name=collection_repo_name), name=role_name.split('.')[2])
    ci_url = "" if not has_ci else content['default']['collection_role_ci_url'].format(git_url=content['default']['collection_git_url'].format(author=author, collection_repo_name=collection_repo_name), name=role_name.split('.')[2])

    role = {
        "ci_badge": ci_badge,
        "ci_url": ci_url,
        "gh_url": content['default']['collection_git_url'].format(author=author, collection_repo_name=collection_repo_name) + f"/tree/main/roles/{role_name.split('.')[2]}",
        "name": role_name,
        "status": status
    }

    for collection in content['ansible_content']['collections']:
        if collection_name in collection['name']:
            collection['roles'].append(role)
            break

def prompt_for_status():
    print("Choose a status:")
    for key, value in STATUSES.items():
        print(f"{key}: {value}")
    print("4: Custom")
    choice = input()
    if choice in STATUSES:
        return STATUSES[choice]
    elif choice == "4":
        return input("Enter custom status: ")
    else:
        print("Invalid choice, defaulting to 'Maintained'.")
        return STATUSES["1"]

def determine_status_from_arg(arg_status):
    status_map = {
        "1": "Maintained",
        "2": "Unmaintained",
        "3": "Deprecated"
    }

    if arg_status in status_map:
        return status_map[arg_status]
    elif arg_status and arg_status not in ["1", "2", "3"]:
        return arg_status
    else:
        return prompt_for_status()

def main():
    parser = argparse.ArgumentParser(description="Manage Ansible content")
    subparsers = parser.add_subparsers(dest='command')

    # Add parsers for the individual commands
    parser_add_role = subparsers.add_parser('add-role', help="Add a new role")
    parser_add_collection = subparsers.add_parser('add-collection', help="Add a new collection")
    parser_sort_content = subparsers.add_parser('sort', help="Sort the collections and roles")

    # Define arguments for 'add-role'
    parser_add_role.add_argument("--role-name", help="Name of the role to add", type=str)
    parser_add_role.add_argument("--ci", help="Whether the role has CI (true/false)", type=str, choices=["true", "false"], default="true")
    parser_add_role.add_argument("--status", default="1", type=str, help='Status of the role. Accepts 1, 2, 3 or custom string.')
    parser_add_role.add_argument("--to-collection", help="Name of the collection to which you want to add the role", type=str)

    # Define arguments for 'add-collection'
    parser_add_collection.add_argument("--collection-name", help="Name of the collection to add", type=str)
    parser_add_collection.add_argument("--status", default="1", type=str, help='Status of the collection. Accepts 1, 2, 3 or custom string.')

    # No additional arguments for 'sort'

    args = parser.parse_args()
    content = load_yaml('content.yml')

    if args.command == 'add-role':
        ci = args.ci == 'true'
        status = determine_status_from_arg(args.status)
        if args.to_collection:
            add_role_to_collection(content, args.role_name, args.to_collection, ci, status)
        else:
            add_new_role(content, args.role_name, ci, status)
    elif args.command == 'add-collection':
        status = determine_status_from_arg(args.status)
        add_new_collection(content, args.collection_name, status)
    elif args.command == 'sort':
        content = sort_content(content)
        save_yaml(content)
        print("Content sorted successfully!")
    else:
        interactive_mode(content)

    # Save the updated content to file only if a command was provided
    if args.command:
        save_yaml(content)
        print("Content updated successfully!")

if __name__ == "__main__":
    main()
