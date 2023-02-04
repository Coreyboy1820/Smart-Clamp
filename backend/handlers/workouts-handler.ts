import database from "../database/database";

export const createWorkout = (req, res) => {
    const query = `INSERT INTO workouts (username, exercise, reps, sets, weight, duration) VALUES ('${req.body.username}', '${req.body.exercise}', '${req.body.reps}', '${req.body.sets}', '${req.body.weight}', '${req.body.duration}')`;
    database.query(query, (err: any, result: any) => {
        if (err) throw err;
        res.send(result);
    });
}

export const readWorkouts = (req, res) => {
    let query = `SELECT * FROM workouts WHERE username = '${req.query.username}'`;
    if (req.query.created_at) {
        query += ` AND DATE(created_at) = '${req.query.created_at}'`;
    }
    if (req.query.exercise) {
        query += ` AND exercise = '${req.query.exercise}'`;
    }
    database.query(query, (err: any, result: any) => {
        if (err) throw err;
        res.send(result);
    });
}

export const updateWorkout = (req, res) => {
    const query = `UPDATE workouts SET username = '${req.body.username}', exercise = '${req.body.exercise}', reps = '${req.body.reps}', sets = '${req.body.sets}', weight = '${req.body.weight}', duration = '${req.body.duration}' WHERE id = '${req.params.id}'`;
    database.query(query, (err: any, result: any) => {
        if (err) throw err;
        res.send(result);
    });
}

export const deleteWorkout = (req, res) => {
    const query = `DELETE FROM workouts WHERE id = '${req.params.id}'`;
    database.query(query, (err: any, result: any) => {
        if (err) throw err;
        res.send(result);
    });
}
