package TaskScheduler;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {

        Scanner scnr = new Scanner(System.in);

        List <Task> taskList = new ArrayList<Task>();
        String task = "";

        System.out.println("Enter today's date (mm/dd): ");
        String[] curPart = scnr.nextLine().split("/");
        int curMonth = Integer.parseInt(curPart[0]);
        int curDay = Integer.parseInt(curPart[1]);

        while (!task.equals("quit")) {
            
            System.out.println("Enter the task (or type 'quit'):");
            task = scnr.nextLine();

            if (!task.equals("quit")) {
                System.out.println("Enter the deadline for the task (mm/dd): ");
                String[] part = scnr.nextLine().split("/");
                int month = Integer.parseInt(part[0]);
                int day = Integer.parseInt(part[1]);
                int deadline = setDeadline(curMonth, curDay, month, day);
                Task taskVar = new Task(task, deadline);
                taskList.add(taskVar);
            }

            TaskScheduler scheduler = new TaskScheduler();
            scheduler.priority(taskList);
            scheduler.printTaskList(scheduler.taskToday);
            
        }
    }
    
    public static int setDeadline(int curMonth, int curDay, int month, int day) {
        int deadline;
        if (curMonth == month) {
            return deadline = day - curDay;
        } else {
        // doesn't matter, as it is greater than 7 any way
            return deadline = 8;
        }
    }       

}

class Task {
    private String task;
    public boolean isCompleted;
    private int deadline;

    public Task(String task, int deadline) {
        this.task = task;
        this.deadline = deadline;
        this.isCompleted = false;
    }

    public String getName() {
        return this.task;
    }

    public int getDeadline() {
        return this.deadline;
    }

    public void isDone(){
        this.isCompleted = true;
    }

    public boolean dueToday() {
        return this.deadline >= 1 && this.deadline < 5;
    }

    public boolean isOverdue() {
        return this.deadline < 1;
    }

    public boolean dueLater() {
        return this.deadline > 7;
    }
}


class TaskScheduler extends Task{

    List <Task> taskToday = new ArrayList<Task>();
    List <Task> taskLater = new ArrayList<Task>();

    public void priority(List<Task> taskList) {
        for (int i = 0; i < taskList.size(); i++) {
            if (taskList.get(i).dueToday() || taskList.get(i).isOverdue()) {
                taskToday.add(taskList.get(i));
            }
            else {
                taskLater.add(taskList.get(i));
            }
        }
    }

    public void deleteTask(List<Task> taskToday, String task) {
        Iterator <Task> iterator = taskToday.iterator();
        while (iterator.hasNext()) {
            Task t = iterator.next();
            if (t.isCompleted()) {
                iterator.remove();
            }
        }
    }
    public void printTaskList(List<Task> taskList) {
        for (Task task : taskToday) {
            System.out.println(task.getName() + " is due today!");
        }
    }

 
}