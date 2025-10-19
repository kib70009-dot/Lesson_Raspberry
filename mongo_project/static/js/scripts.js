document.addEventListener("DOMContentLoaded", () => {
    const todoForm = document.getElementById("todo-form");
    const todoList = document.getElementById("todo-list");
    const todoName = document.getElementById("todo-name");
    const todoDescription = document.getElementById("todo-description");

    async function fetchTodos() {
        const response = await fetch("/todos/");
        const todos = await response.json();
        todoList.innerHTML = "";
        todos.forEach(todo => {
            const li = document.createElement("li");
            li.textContent = `${todo.name} - ${todo.description || ""}`;

            const deleteButton = document.createElement("button");
            deleteButton.textContent = "Delete";
            deleteButton.addEventListener("click", async () => {
                await fetch(`/todos/${todo._id}`, { method: "DELETE" });
                fetchTodos();
            });

            const editButton = document.createElement("button");
            editButton.textContent = "Edit";
            editButton.addEventListener("click", async () => {
                const newName = prompt("Enter new name:", todo.name);
                const newDescription = prompt("Enter new description:", todo.description);

                if (newName !== null && newDescription !== null) {
                    await fetch(`/todos/${todo._id}`, {
                        method: "PUT",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ ...todo, name: newName, description: newDescription, completed: false })
                    });
                    fetchTodos();
                }
            });

            li.appendChild(editButton);
            li.appendChild(deleteButton);
            todoList.appendChild(li);
        });
    }

    todoForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        await fetch("/todos/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: todoName.value,
                description: todoDescription.value
            })
        });
        todoName.value = "";
        todoDescription.value = "";
        fetchTodos();
    });

    fetchTodos();
});
