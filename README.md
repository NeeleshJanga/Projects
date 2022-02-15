# Projetcs
The projects that I have finished will be available here.


package com.NeeleshServlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/add")
public class AddServlet extends HttpServlet{
	
	// service is a must method to keep & works with both get and post methods
	public void service (HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException {
		int i = Integer.parseInt(req.getParameter("Num_1"));
		int j = Integer.parseInt(req.getParameter("Num_2"));		
		
		int k = i + j;
		
//		System.out.println("Result is " + k);
		
//		res.getWriter().print("Result is " + k);
		
//		PrintWriter pw = res.getWriter();

//		Making other servlets to refer to the data
//		req.setAttribute("K value", k);
		
//		setAttribute and getAttributes can by type casted using primitive types but get Parameter and setParameter must
//		be parsed

		
/*
 * RequestDispatcher:
 		Defines an object that receives requests from the client and sends them to any resource (such as a servlet,HTML file
 		, or JSP file) on the server. The servlet container creates the RequestDispatcher object,which is used as a wrapper 
 		around a server resource located at a particular path or given by a particular name. This interface is intended to 
 		wrap servlets,but a servlet container can create RequestDispatcherobjects to wrap any type of resource.
 */
//		RequestDispatcher rd =  req.getRequestDispatcher("sq");
//		Sending req object and res object to sq servlet
//		rd.forward(req, res);
//		Getting error if the below data is uncommented
//		Sending data to sq servlet
//		req.setAttribute("K value", k);
		
/*		If we want to access the stored attribute in request object, i.e, 'K value',
		from other servlet we need to redirect it as follows..
*/
//		res.sendRedirect("sq?K value=" + k);
		
/*
 * Session:
 		- Web application maintains session for users when opened
 		- This session maintenance will be done by Tomcat here in this case
 		- If we can put our data in session instead of putting in request objects
 		  the data is available through out the session and could be accessed to all
 		  the servlets used or called in that session.
 		- This concept is called Session Management
 */
//		HttpSession session = req.getSession();
//		session.setAttribute("K value", k);
//		
//		res.sendRedirect("sq");
		
//		Removing attribute from session
//		session.removeAttribute("K value");
		
/*
 * Cookies:
 		- Cookie cookie = new Cookie(String name, String value);
 		- Client side i.e, we use response object to initiate something
 		- Similar to session but session is at server side
 		- Cookie is related as a buss pass i.e, when ever u go a ride we can show that pass
 		- res.addCookie(cookie) sends cookie to the client (server) and client 
 		- Benefit with cookies is that when client requests to a servlet the cookies are sent along with it by default
 		- So it is mandatory to the requesting servlets to accept the cookies
 */
//		Cookie cookie = new Cookie("K", k + "");
////		Sending the cookie to client
//		res.addCookie(cookie);
////		Redirecting to sq servlet
//		res.sendRedirect("sq");
//		
//		req.removeAttribute("K value");
		

/*
 * ServletConfig & ServletContext:
 		- They both are interfaces
 		- 
 */
//		PrintWriter out = res.getWriter();
//		out.print("Hi<br>");
		
//		When we directly call 'getServletContext()' it is obtained from 'HttpServlet'
//		ServletContext servletContext = req.getServletContext();
//		We can also call 'req.getServletContext()' but it is obtained form request object
//		ServletContext servletContext2 = req.getServletContext();
		
//		To get values of attributes written in XML file we use 'getInitParameter(String attribute)'
//		getInitParameter is a method
//		String name = servletContext.getInitParameter("name");
		
//		out.println(name)

		
		
		
		
//		JSP
		
		PrintWriter out = res.getWriter();
		out.println("<html> <body bgcolor='grey'>");
		out.println("Output : " + k);
		out.println("</body></html>");
		
		
		
		
		
		
		
		
	}
	
	
//	// Works only with the post method
//	public void doPost (HttpServletRequest req, HttpServletResponse res) throws IOException {
//		int i = Integer.parseInt(req.getParameter("Num_1"));
//		int j = Integer.parseInt(req.getParameter("Num_2"));		
//		
//		int k = i + j;
//		
////		System.out.println("Result is " + k);
//		
//		res.getWriter().println("Result is " + k);
//	}
//	
//	
//	public void doGet (HttpServletRequest req, HttpServletResponse res) throws IOException {
//		int i = Integer.parseInt(req.getParameter("Num_1"));
//		int j = Integer.parseInt(req.getParameter("Num_2"));		
//		
//		int k = i + j;
//		
////		System.out.println("Result is " + k);
//		
//		res.getWriter().println("Result is " + k);
//	}
	
}
