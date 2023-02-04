import express from "express";
import { getWorkouts, addWorkout, updateWorkout, deleteWorkout } from "../handlers/workouts-handler";

const workoutsRoute = express.Router();

workoutsRoute.get("/", getWorkouts);
workoutsRoute.post("/", addWorkout);
workoutsRoute.put("/:id", updateWorkout);
workoutsRoute.delete("/:id", deleteWorkout);

export default workoutsRoute;