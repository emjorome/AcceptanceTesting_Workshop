Feature: To-Do List Manager
  As a user
  I want to manage my tasks
  So that I can organize my work

  # Escenario 1
  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with priority "High"
    Then the to-do list should contain "Buy groceries"

  # Escenario 2
  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          | Priority |
      | Buy groceries | High     |
      | Pay bills     | Normal   |
    When the user lists all tasks
    Then the output should contain:
      | Output        |
      | Buy groceries |
      | Pay bills     |

  # Escenario 3
  Scenario: Mark a task as completed
    Given the to-do list contains tasks with status:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  # Escenario 4
  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  # Escenario 5
  Scenario: Delete a specific task
    Given the to-do list contains tasks:
      | Task         |
      | Walk the dog |
      | Wash car     |
    When the user deletes the task "Walk the dog"
    Then the to-do list should not contain "Walk the dog"
