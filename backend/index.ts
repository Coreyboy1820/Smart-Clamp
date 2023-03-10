import express from "express";
import cors from 'cors'

import workoutsRoute from "./routes/workouts-route";

const port = 5000;
const app = express();

app.use(cors());
app.use(express.json({ limit: "2mb" }));
app.use(express.urlencoded({ extended: true }));

app.use("/workouts", workoutsRoute);

app.get("/", (req, res) => {
    res.send("Smart Clamp API");
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:5000`);
});