const bcrypt = require('bcryptjs');

const testPassword = async () => {
  const plainPassword = "password123"; // Replace with the plain text password
  const hashedPassword = "$2a$10$yIKPt8lNKO9Dz7EYfWm12uZHaS04wvREzF6DacywFRMLgO9SxR7KK"; // Replace with the hashed password from your database

  const isMatch = await bcrypt.compare(plainPassword, hashedPassword);
  console.log("Password Match:", isMatch); // Should print true if the password matches
};

testPassword();
