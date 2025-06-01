const bcrypt = require('bcryptjs');

const testHash = async () => {
    const plainPassword = "123456789"; // Your plain password
    const hash = await bcrypt.hash(plainPassword, 10);
    console.log("Re-hashed Password:", hash);
};


testHash();
