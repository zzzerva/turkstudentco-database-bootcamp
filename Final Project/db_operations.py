import psycopg2
from psycopg2 import Error
import datetime
import hashlib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters
DB_NAME = os.getenv("DB_NAME", "online_education_platform")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_connection():
    """Establish a connection to the PostgreSQL database"""
    try:
        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return connection
    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_member(username, email, password, first_name, last_name):
    """Register a new member"""
    connection = get_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if username or email already exists
        cursor.execute("SELECT member_id FROM members WHERE username = %s OR email = %s", 
                      (username, email))
        if cursor.fetchone():
            return False, "Username or email already exists"
        
        # Insert new member
        hashed_password = hash_password(password)
        cursor.execute(
            "INSERT INTO members (username, email, password, first_name, last_name) VALUES (%s, %s, %s, %s, %s) RETURNING member_id",
            (username, email, hashed_password, first_name, last_name)
        )
        member_id = cursor.fetchone()[0]
        
        connection.commit()
        return True, f"Member registered successfully with ID: {member_id}"
    
    except Error as e:
        return False, f"Error registering member: {e}"
    
    finally:
        if connection:
            connection.close()

def enroll_member_in_course(member_id, course_id):
    """Enroll a member in a course"""
    connection = get_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if member exists
        cursor.execute("SELECT member_id FROM members WHERE member_id = %s", (member_id,))
        if not cursor.fetchone():
            return False, "Member not found"
        
        # Check if course exists
        cursor.execute("SELECT course_id FROM courses WHERE course_id = %s", (course_id,))
        if not cursor.fetchone():
            return False, "Course not found"
        
        # Check if already enrolled
        cursor.execute("SELECT enrollment_id FROM enrollments WHERE member_id = %s AND course_id = %s", 
                      (member_id, course_id))
        if cursor.fetchone():
            return False, "Member already enrolled in this course"
        
        # Insert enrollment
        cursor.execute(
            "INSERT INTO enrollments (member_id, course_id) VALUES (%s, %s) RETURNING enrollment_id",
            (member_id, course_id)
        )
        enrollment_id = cursor.fetchone()[0]
        
        connection.commit()
        return True, f"Enrollment successful with ID: {enrollment_id}"
    
    except Error as e:
        return False, f"Error enrolling member: {e}"
    
    finally:
        if connection:
            connection.close()

def create_certificate(course_id, certificate_code):
    """Create a new certificate for a course"""
    connection = get_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if course exists
        cursor.execute("SELECT course_id FROM courses WHERE course_id = %s", (course_id,))
        if not cursor.fetchone():
            return False, "Course not found"
        
        # Check if certificate code already exists
        cursor.execute("SELECT certificate_id FROM certificates WHERE certificate_code = %s", (certificate_code,))
        if cursor.fetchone():
            return False, "Certificate code already exists"
        
        # Insert certificate
        cursor.execute(
            "INSERT INTO certificates (certificate_code, course_id) VALUES (%s, %s) RETURNING certificate_id",
            (certificate_code, course_id)
        )
        certificate_id = cursor.fetchone()[0]
        
        connection.commit()
        return True, f"Certificate created successfully with ID: {certificate_id}"
    
    except Error as e:
        return False, f"Error creating certificate: {e}"
    
    finally:
        if connection:
            connection.close()

def assign_certificate_to_member(member_id, certificate_id):
    """Assign a certificate to a member"""
    connection = get_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if member exists
        cursor.execute("SELECT member_id FROM members WHERE member_id = %s", (member_id,))
        if not cursor.fetchone():
            return False, "Member not found"
        
        # Check if certificate exists
        cursor.execute("SELECT certificate_id FROM certificates WHERE certificate_id = %s", (certificate_id,))
        if not cursor.fetchone():
            return False, "Certificate not found"
        
        # Check if already assigned
        cursor.execute("SELECT assignment_id FROM certificate_assignments WHERE member_id = %s AND certificate_id = %s", 
                      (member_id, certificate_id))
        if cursor.fetchone():
            return False, "Certificate already assigned to this member"
        
        # Insert assignment
        cursor.execute(
            "INSERT INTO certificate_assignments (member_id, certificate_id) VALUES (%s, %s) RETURNING assignment_id",
            (member_id, certificate_id)
        )
        assignment_id = cursor.fetchone()[0]
        
        connection.commit()
        return True, f"Certificate assigned successfully with ID: {assignment_id}"
    
    except Error as e:
        return False, f"Error assigning certificate: {e}"
    
    finally:
        if connection:
            connection.close()

def create_blog_post(member_id, title, content):
    """Create a new blog post"""
    connection = get_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if member exists
        cursor.execute("SELECT member_id FROM members WHERE member_id = %s", (member_id,))
        if not cursor.fetchone():
            return False, "Member not found"
        
        # Insert blog post
        cursor.execute(
            "INSERT INTO blog_posts (title, content, author_id) VALUES (%s, %s, %s) RETURNING post_id",
            (title, content, member_id)
        )
        post_id = cursor.fetchone()[0]
        
        connection.commit()
        return True, f"Blog post created successfully with ID: {post_id}"
    
    except Error as e:
        return False, f"Error creating blog post: {e}"
    
    finally:
        if connection:
            connection.close()

def get_member_courses(member_id):
    """Get all courses a member is enrolled in"""
    connection = get_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if member exists
        cursor.execute("SELECT member_id FROM members WHERE member_id = %s", (member_id,))
        if not cursor.fetchone():
            return False, "Member not found"
        
        # Get courses
        cursor.execute("""
            SELECT c.course_id, c.course_name, c.description, c.start_date, c.end_date, c.instructor, cat.category_name
            FROM enrollments e
            JOIN courses c ON e.course_id = c.course_id
            JOIN categories cat ON c.category_id = cat.category_id
            WHERE e.member_id = %s
        """, (member_id,))
        
        courses = cursor.fetchall()
        
        if not courses:
            return True, "Member is not enrolled in any courses"
        
        # Format results
        result = []
        for course in courses:
            result.append({
                "course_id": course[0],
                "course_name": course[1],
                "description": course[2],
                "start_date": course[3],
                "end_date": course[4],
                "instructor": course[5],
                "category": course[6]
            })
        
        return True, result
    
    except Error as e:
        return False, f"Error getting member courses: {e}"
    
    finally:
        if connection:
            connection.close()

def get_member_certificates(member_id):
    """Get all certificates a member has earned"""
    connection = get_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if member exists
        cursor.execute("SELECT member_id FROM members WHERE member_id = %s", (member_id,))
        if not cursor.fetchone():
            return False, "Member not found"
        
        # Get certificates
        cursor.execute("""
            SELECT c.certificate_id, c.certificate_code, c.issue_date, co.course_name, co.course_id
            FROM certificate_assignments ca
            JOIN certificates c ON ca.certificate_id = c.certificate_id
            JOIN courses co ON c.course_id = co.course_id
            WHERE ca.member_id = %s
        """, (member_id,))
        
        certificates = cursor.fetchall()
        
        if not certificates:
            return True, "Member has not earned any certificates"
        
        # Format results
        result = []
        for cert in certificates:
            result.append({
                "certificate_id": cert[0],
                "certificate_code": cert[1],
                "issue_date": cert[2],
                "course_name": cert[3],
                "course_id": cert[4]
            })
        
        return True, result
    
    except Error as e:
        return False, f"Error getting member certificates: {e}"
    
    finally:
        if connection:
            connection.close()

def get_member_blog_posts(member_id):
    """Get all blog posts by a member"""
    connection = get_connection()
    if not connection:
        return False, "Database connection failed"
    
    try:
        cursor = connection.cursor()
        
        # Check if member exists
        cursor.execute("SELECT member_id FROM members WHERE member_id = %s", (member_id,))
        if not cursor.fetchone():
            return False, "Member not found"
        
        # Get blog posts
        cursor.execute("""
            SELECT post_id, title, content, publication_date
            FROM blog_posts
            WHERE author_id = %s
            ORDER BY publication_date DESC
        """, (member_id,))
        
        posts = cursor.fetchall()
        
        if not posts:
            return True, "Member has not created any blog posts"
        
        # Format results
        result = []
        for post in posts:
            result.append({
                "post_id": post[0],
                "title": post[1],
                "content": post[2],
                "publication_date": post[3]
            })
        
        return True, result
    
    except Error as e:
        return False, f"Error getting member blog posts: {e}"
    
    finally:
        if connection:
            connection.close()

# Example usage
if __name__ == "__main__":
    # Register a new member
    success, message = register_member(
        username="johndoe",
        email="john.doe@example.com",
        password="securepassword123",
        first_name="John",
        last_name="Doe"
    )
    print(message)
    
    if success and isinstance(message, str) and "ID:" in message:
        member_id = int(message.split("ID:")[1].strip())
        
        # Create a course (assuming category_id 1 exists)
        connection = get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO courses (course_name, description, start_date, end_date, instructor, category_id)
                    VALUES (%s, %s, %s, %s, %s, %s) RETURNING course_id
                """, (
                    "Introduction to PostgreSQL",
                    "Learn the basics of PostgreSQL database management",
                    datetime.date.today(),
                    datetime.date.today() + datetime.timedelta(days=30),
                    "Jane Smith",
                    1
                ))
                course_id = cursor.fetchone()[0]
                connection.commit()
                print(f"Course created with ID: {course_id}")
                
                # Enroll member in course
                success, message = enroll_member_in_course(member_id, course_id)
                print(message)
                
                # Create certificate
                success, message = create_certificate(course_id, "CERT-001")
                print(message)
                
                if success and isinstance(message, str) and "ID:" in message:
                    certificate_id = int(message.split("ID:")[1].strip())
                    
                    # Assign certificate to member
                    success, message = assign_certificate_to_member(member_id, certificate_id)
                    print(message)
                
                # Create blog post
                success, message = create_blog_post(
                    member_id,
                    "My Learning Journey",
                    "I started learning PostgreSQL today and it's amazing!"
                )
                print(message)
                
                # Get member courses
                success, message = get_member_courses(member_id)
                if success and isinstance(message, list):
                    print("\nMember's courses:")
                    for course in message:
                        print(f"- {course['course_name']} ({course['category']})")
                
                # Get member certificates
                success, message = get_member_certificates(member_id)
                if success and isinstance(message, list):
                    print("\nMember's certificates:")
                    for cert in message:
                        print(f"- {cert['certificate_code']} for {cert['course_name']}")
                
                # Get member blog posts
                success, message = get_member_blog_posts(member_id)
                if success and isinstance(message, list):
                    print("\nMember's blog posts:")
                    for post in message:
                        print(f"- {post['title']} ({post['publication_date']})")
                
            except Error as e:
                print(f"Error: {e}")
            finally:
                connection.close() 