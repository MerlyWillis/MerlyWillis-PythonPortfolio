# Priority Task Manager.

task_manager = {}

def add_task(task, priority):
    task_manager[task] = priority
    print(f'{task} successfully added with priority level {priority}.')

def remove_task(task):
    if task not in task_manager:
        print(f'{task} not in Task Manager!')
    else:
        del task_manager[task]
        print(f'{task} successfully removed from Task Manager.')
        
def view_tasks():
    if not task_manager:
        print('No Tasks in Task Manager!')
    else:
        print('Tasks:')
        for task, priority in sorted(task_manager.items(), key=lambda x: x[1]):
            print(f'Task: {task}: Priority: {priority}')
            

while True:
    print('Welcome to the Task Manager!')
    print('Please choose an option from the list below.')
    print('1. Add a Task')
    print('2. Remove a Task')
    print('3. View Tasks')
    print('4. Exit')
    choice = input('Enter Choice: ')
    
    if choice == '1':
        task = input('Enter Task Name: ')
        priority = input('Enter Priority Level (1-3): ')
        add_task(task, priority)
    elif choice == '2':
        task = input('Enter Task Name: ')
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print('Thanks for using the Task Manager, goodbye.')
        break
    else:
        print('Invalid entry, please enter a choice (1-4).')