package TaskScheduler;
import java.util.Scanner;
import java.time.LocalDate;
import java.time.Month;

public class Main {
    public static void main(String[] args) {
        
        //get input from the user

        Scanner scnr = new Scanner(System.in);
        System.out.println("Enter the task:");
        String task = scnr.nextLine();

        System.out.printf("Enter the deadline for the '%s' (month/day): ", task);

        String[] part = scnr.nextLine().split(" ");

        Month month = Month.valueOf(part[0].toUpperCase());
        int day = Integer.parseInt(part[1]);

        LocalDate curDate = LocalDate.of(LocalDate.now().getYear(), month, day);

        System.out.println(curDate);
        if (curDate.isBefore(LocalDate.now())) {
            System.out.println("Invalid date");
            return;
        }
    }


}

class Task {
    private String task;
    private boolean isCompleted;
    private LocalDate deadline;

    public Task(String task, LocalDate deadline) {
        this.task = task;
        this.deadline = deadline;
        this.isCompleted = false;
    }

    public String getName() {
        return this.task;
    }

    public LocalDate getDeadline() {
        return this.deadline;
    }

    public void isDone(){
        this.isCompleted = true;
    }

    public boolean dueToday() {
        int daysBefore = 
        return this.deadline.isEqual(LocalDate.now());
    }
}
