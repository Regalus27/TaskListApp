# First, we have a Task. This is the base unit of the whole app.
# Each Task has a name, description, and an estimated effort value when created.
testTask = {
    "name": "Taskname",
    "description": "Lorum Ipsum Dolor",
    "estimatedEffort": "Low",
    "completedEffort": "Low"
}


# Now, we need to automate the creation of tasks in some way, as it wouldn't do to force the user to make their own.
def makeTask(name, description, estimatedEffort, completedEffort):
    task = {
        # "What should we call this Task?"
        "Name": name,
        # "Are there any additional details you want to write down about this Task?"
        "Description": description,
        # "How hard do you think this Task will be to complete?"
        "Estimated Effort": estimatedEffort,
        # "How hard was this Task to complete?"
        "Completed Effort": completedEffort
    }

    return task


newTask = makeTask("Test this out", "Make a test, see if we can print it", 1, 1)
for i in newTask:
    print(newTask.get(i))


# We need something to store these Tasks in, preferably something with easily accessible data for sorting.

