import database from "../database/database";

export const createWorkout = (req, res) => {
    const query = `INSERT INTO workouts (username, exercise, reps, weight, duration) VALUES ('${req.body.username}', '${req.body.exercise}', '${req.body.reps}', '${req.body.weight}', '${req.body.duration}')`;
    database.query(query, (err: any, result: any) => {
        if (err) {
            res.send("Error POST /workouts");
        }
        res.send(result);
    });
}

export const readWorkouts = (req, res) => {
    let query = "";
    if (req.query.username) {
        query = `SELECT * FROM workouts WHERE username = '${req.query.username}'`;
    }
    else {
        query = `SELECT * FROM workouts`;
    }
    database.query(query, (err: any, result: any) => {
        if (err) {
            res.send("Error GET /workouts");
        }
        res.send(result);
    });
}

export const updateWorkout = (req, res) => {
    const query = `UPDATE workouts SET username = '${req.body.username}', exercise = '${req.body.exercise}', reps = '${req.body.reps}', weight = '${req.body.weight}', duration = '${req.body.duration}' WHERE id = '${req.params.id}'`;
    database.query(query, (err: any, result: any) => {
        if (err) {
            res.send("Error PUT /workouts");
        }
        res.send(result);
    });
}

export const deleteWorkout = (req, res) => {
    const query = `DELETE FROM workouts WHERE id = '${req.params.id}'`;
    database.query(query, (err: any, result: any) => {
        if (err) {
            res.send("Error DELETE /workouts");
        }
        res.send(result);
    });
}
