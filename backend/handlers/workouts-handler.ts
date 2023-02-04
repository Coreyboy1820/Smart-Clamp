import database from "../database/database";

export const getWorkouts = (req, res) => {
    res.send("Get workouts");
}

export const addWorkout = (req, res) => {
    res.send("Add workout");
}

export const updateWorkout = (req, res) => {
    res.send("Update workout");
}

export const deleteWorkout = (req, res) => {
    res.send("Delete workout");
}
