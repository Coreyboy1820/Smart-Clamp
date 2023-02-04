import express from "express";
import { readWorkouts, createWorkout, updateWorkout, deleteWorkout } from "../handlers/workouts-handler";

const workoutsRoute = express.Router();

workoutsRoute.get("/", readWorkouts);
workoutsRoute.post("/", createWorkout);
workoutsRoute.put("/:id", updateWorkout);
workoutsRoute.delete("/:id", deleteWorkout);

export default workoutsRoute;