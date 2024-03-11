package TaskScheduler;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

// This program can aid as a task prioritization for students.
// The code asks for a user input and stores the tasks in a list, then it 
// filters the tasks based on the priority and the deadline

public class Task {
    private String task;
    private int deadline;
    public boolean priority;
//constructor
    public Task(String task, int deadline, boolean priority) {
        this.task = task;
        this.deadline = deadline;
        this.priority = priority;
    }

//methods of setting and getting the values
    public boolean setPriority(boolean priority) {
        return this.priority = priority;
    }

    public String getName() {
        return this.task;
    }

    public boolean dueToday() {
        return this.deadline >= 1 && this.deadline < 5;
    }

    public boolean dueLater() {
        return this.deadline > 5;
    }
    
}

class Main {
    public static void main(String[] args) {

        Scanner scnr = new Scanner(System.in);

        List <Task> taskList = new ArrayList<Task>();
        String task = "";
//storing the current date as an int
        System.out.println("Enter today's date (mm/dd): ");
        String[] curPart = scnr.nextLine().split("/");
        int curMonth = Integer.parseInt(curPart[0]);
        int curDay = Integer.parseInt(curPart[1]);

//getting the input (tasks, priiority and deadline) from the user
        while (!task.equals("quit")) {
            System.out.println("Enter the task (or type 'quit'):");
            task = scnr.nextLine();
            
            if (!task.equals("quit")) {
                System.out.println("Is this task a high priority? (y/n): ");
                String priority1 = scnr.nextLine();
                boolean priority = priority1.equalsIgnoreCase("y");
                System.out.println("Enter the deadline for the task (mm/dd): ");
            // storing the deadline as an int
                String[] part = scnr.nextLine().split("/");
                int month = Integer.parseInt(part[0]);
                int day = Integer.parseInt(part[1]);
                int deadline = setDeadline(curMonth, curDay, month, day);
            // creating a new task object and adding it to the list
                Task newTask = new Task(task, deadline, priority);
                taskList.add(newTask);
            }
        }
// creating a new TaskScheduler object and calling the method to prioritize and filter the tasks
        TaskScheduler scheduler = new TaskScheduler();
        scheduler.priority(taskList);
        scheduler.printTaskList(taskList);
    }

// method to set the deadline and make sure the days aligns
    public static int setDeadline(int curMonth, int curDay, int month, int day) {
        if (curMonth == month) {
            return day - curDay;
        } else if ((curMonth>month) || (curMonth<=month && curDay>day)) {
            return 0;
        } else {
// doesn't matter, as it is greater than 5 any way, so it will be considered as due later
            return 6;
        }
    }      
}

class TaskScheduler {
//storing the tasks in two different lists
    List <Task> taskToday = new ArrayList<Task>();
    List <Task> taskLater = new ArrayList<Task>();

// method to prioritize the tasks and filter them
    public void priority(List<Task> taskList) {
        for (Task task : taskList) {
            if (task.dueToday() && task.priority) {
                taskToday.add(task);
            } else if (task.dueLater() && task.priority) {
                taskToday.add(task);
            } else if (task.dueToday() && !task.priority) {
                taskToday.add(task);
            } else {
                taskLater.add(task);
            
            }
        }
    }
// method to print the tasks with a whitespace
    public void printTaskList(List<Task> taskList) {
        System.out.println("Your tasks due today are: ");
        for (Task task : taskToday) {
            System.out.printf(" %15s is due%n", task.getName());
        }
    }
}
