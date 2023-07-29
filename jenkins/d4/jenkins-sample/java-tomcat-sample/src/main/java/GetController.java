import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import dao.GetDao;
import model.Users;

/**
 * Servlet implementation class GetController
 */
public class GetController extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int aid = Integer.parseInt(request.getParameter("emp_no"));
        GetDao dao  = new GetDao();
        Users a1 = dao.getUser(aid);
        HttpSession session = request.getSession();
        session.setAttribute("user_attr", a1);
        response.sendRedirect("showUser.jsp");
    }
}