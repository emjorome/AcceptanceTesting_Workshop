from behave import given, when, then
from todo_list import ToDoListManager


# ---------- GIVEN ----------

@given("the to-do list is empty")
def step_impl(context):
    context.manager = ToDoListManager()


@given("the to-do list contains tasks:")
def step_impl(context):
    context.manager = ToDoListManager()
    for row in context.table:
        # Si existe columna Priority la usamos, si no, usamos "Normal"
        priority = row.get("Priority", "Normal")
        context.manager.add_task(row["Task"], priority=priority)


@given("the to-do list contains tasks with status:")
def step_impl(context):
    context.manager = ToDoListManager()
    for row in context.table:
        task_name = row["Task"]
        status = row["Status"]
        context.manager.add_task(task_name)  # status inicial Pending
        if status.lower() == "completed":
            context.manager.mark_task_completed(task_name)


# ---------- WHEN ----------

@when('the user adds a task "{name}" with priority "{priority}"')
def step_impl(context, name, priority):
    context.manager.add_task(name, priority=priority)


@when("the user lists all tasks")
def step_impl(context):
    context.list_output = context.manager.list_tasks()


@when('the user marks task "{name}" as completed')
def step_impl(context, name):
    context.manager.mark_task_completed(name)


@when("the user clears the to-do list")
def step_impl(context):
    context.manager.clear_list()


@when('the user deletes the task "{name}"')
def step_impl(context, name):
    context.manager.delete_task(name)


# ---------- THEN ----------

@then('the to-do list should contain "{name}"')
def step_impl(context, name):
    task_names = [t.name for t in context.manager.tasks]
    assert name in task_names, f'Task "{name}" not found in list {task_names}'


@then("the output should contain:")
def step_impl(context):
    # list_tasks devuelve lista de strings o "No tasks found."
    if isinstance(context.list_output, list):
        output_str = "\n".join(context.list_output)
    else:
        output_str = str(context.list_output)

    for row in context.table:
        expected = row["Output"]
        assert expected in output_str, f'Expected "{expected}" in output "{output_str}"'


@then('the to-do list should show task "{name}" as completed')
def step_impl(context, name):
    for task in context.manager.tasks:
        if task.name == name:
            assert task.status == "Completed", (
                f'Task "{name}" status is {task.status}, expected Completed'
            )
            return
    assert False, f'Task "{name}" not found'


@then("the to-do list should be empty")
def step_impl(context):
    assert len(context.manager.tasks) == 0, "List is not empty"


@then('the to-do list should not contain "{name}"')
def step_impl(context, name):
    task_names = [t.name for t in context.manager.tasks]
    assert name not in task_names, f'Task "{name}" should have been deleted'
