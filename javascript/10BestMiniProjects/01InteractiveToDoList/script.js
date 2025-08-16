// Get references to HTML elements
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');

// Load tasks from local storage if available
const tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Function to add a new task
function addTask(){
	const taskText = taskInput.value.trim();
	if(taskText !== ''){
		const task = {text:taskText, completed:false};
		tasks.push(task);
		updateTasks();
		taskInput.value = '';
	}
}

// Function to update the task list
function updateTasks(){
	// Clear the task list
	taskList.innerHTML='';

	// Update local storage
	localStorage.setItem('tasks', JSON.stringify(tasks));

	// Add tasks to the list
	tasks.forEach((task, index)=>{
		const li = document.createElement('li');
		li.innerHTML = `
			<span class="${task.completed?'completed':''}">${task.text}</span>
			<button onclick="toggleTask(${index})">Mark ${task.completed?'Incomplete':'Complete'}</button>
			<button onclick="deleteTask(${index})">Delete</button>
		`;
		taskList.appendChild(li);
	})
}

// Function to toggle task completion
function toggleTask(index){
	tasks[index].completed = !tasks[index].completed;
	updateTasks();
}

// Function to delete a task
function deleteTask(index){
	tasks.splice(index,1);
	updateTasks();
}

// Initial update of the task list
updateTasks();
