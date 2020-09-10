USE python_mysql;

DELIMITER $$

CREATE PROCEDURE find_by_isbn(
	IN p_isbn VARCHAR(13),
    OUT p_title VARCHAR(255)
)
BEGIN
	SELECT title 
    INTO p_title 
    FROM books
	WHERE isbn = p_isbn;
END$$

DELIMITER ;