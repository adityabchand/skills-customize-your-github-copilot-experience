---
agent: agent
description: Create a new programming homework assignment following assignment standards
argument-hint: Provide assignment details (topic, objectives, tasks)
---

# 📘 Create New Programming Assignment

Your goal is to generate a new homework assignment for students following project standards and learning best practices.

## Step 1: Gather Assignment Information

If not already provided by the user, ask for the following details:
- **Assignment topic**: What will students build or learn?
- **Learning objectives**: What key skills should students practice?
- **Tasks**: What specific tasks or requirements should students complete?
- **Due date**: When is it due? (Default: 7 days from today)
- **Starter code needed**: Should starter code or templates be provided?

## Step 2: Create Assignment Structure

1. Create a new directory in the `assignments` folder with a unique, descriptive name (e.g., `loops-and-conditionals`, `file-handling`)
2. Create a `README.md` file in the directory following the structure defined in [.github/instructions/assignments.instructions.md](./.github/instructions/assignments.instructions.md)
3. Use the proper format:
   - **Title**: `# 📘 Assignment: [Title]`
   - **Objective**: `## 🎯 Objective` with clear learning goals and "Skills practiced:" line
   - **Tasks**: `## 📝 Tasks` with multiple tasks using `### 🛠️ [Task Name]`
   - Each task must have `#### Description` and `#### Requirements` sections
4. (Optional) Add starter code or support files:
   - Save as `starter-code.py` or similar
   - Include a sample or template for students to build upon

## Step 3: Update Website Configuration

Update the assignments list in [config.json](../../config.json) to include the new assignment:
- Add an entry with `name`, `description`, `folder`, and `dueDate`
- For `dueDate`, use the current date plus 7 days (format: YYYY-MM-DD) unless specified otherwise

## Reference

For detailed guidelines on assignment structure and best practices, see [.github/instructions/assignments.instructions.md](./.github/instructions/assignments.instructions.md).