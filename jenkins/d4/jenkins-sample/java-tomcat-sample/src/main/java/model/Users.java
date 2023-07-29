package model;

public class Users
{
    private int emp_no;
    private String first_name;
    private String last_name;
    private String title;
    public int getEmpno() {
        return emp_no;
    }
    public void setEmpno(int emp_no) {
        this.emp_no = emp_no;
    }
    public String getFirst_name() {
        return first_name;
    }
    public void setFirstname(String first_name) {
        this.first_name = first_name;
    }
    public String getLastname() {
        return last_name;
    }
    public void setLastname(String last_name) {
        this.last_name = last_name;
    }
    public String getTitle() {
        return title;
    }
    public void setTitle(String last_name) {
        this.title = title;
    }
    @Override
    public String toString() {
        return "employees [emp_no=" + emp_no + ", first_name=" + first_name + ", last_name=" + last_name + ", title=" + title + "]";
    }
}