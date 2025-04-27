-- Çevrimiçi Eğitim Platformu Veritabanı Şeması

-- Tabloları bağımlıklarının ters sıralamasıyla silin
DROP TABLE IF EXISTS certificate_assignments;
DROP TABLE IF EXISTS certificates;
DROP TABLE IF EXISTS blog_posts;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS members;


CREATE TABLE members (
    member_id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    profile_level INTEGER NOT NULL DEFAULT 1
);


CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE courses (
    course_id BIGSERIAL PRIMARY KEY,
    course_name VARCHAR(200) NOT NULL,
    course_description TEXT,
    starting_date DATE NOT NULL,
    ending_date DATE NOT NULL,
    instructor VARCHAR(100) NOT NULL,
    category_id SMALLINT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);


CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    member_id BIGINT NOT NULL,
    course_id BIGINT NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completion_status BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE (member_id, course_id)
);


CREATE TABLE certificates (
    certificate_id BIGSERIAL PRIMARY KEY,
    certificate_code VARCHAR(100) NOT NULL UNIQUE,
    course_id BIGINT NOT NULL,
    issue_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


CREATE TABLE certificate_assignments (
    assignment_id BIGSERIAL PRIMARY KEY,
    member_id BIGINT NOT NULL,
    certificate_id BIGINT NOT NULL,
    assignment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (certificate_id) REFERENCES certificates(certificate_id),
    UNIQUE (member_id, certificate_id)
);


CREATE TABLE blog_posts (
    post_id BIGSERIAL PRIMARY KEY,
    blog_title VARCHAR(255) NOT NULL,
    blog_content TEXT NOT NULL,
    publication_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author_id BIGINT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES members(member_id)
);


INSERT INTO categories (category_name) VALUES
    ('Yapay Zeka'),
    ('Blok Zincir'),
    ('Siber Güvenlik'),
    ('Web Geliştirme'),
    ('Veri Tabanı Yönetimi');


CREATE INDEX idx_enrollments_member_id ON enrollments(member_id);
CREATE INDEX idx_enrollments_course_id ON enrollments(course_id);
CREATE INDEX idx_certificate_assignments_member_id ON certificate_assignments(member_id);
CREATE INDEX idx_certificate_assignments_certificate_id ON certificate_assignments(certificate_id);
CREATE INDEX idx_blog_posts_author_id ON blog_posts(author_id); 