import mysql from "mysql";

const database = mysql.createConnection({
    host: 'cruzhacks-2023-db.cfxqvwupnsia.us-west-1.rds.amazonaws.com',
    user: 'admin',
    password: 'password',
    database: 'smartweight'
})

database.connect((err) => {
    if (err) throw err;
    console.log("Database connected!");
});

export default database;