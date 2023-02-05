import { WorkoutsDTO } from "../../dto/workouts.dto";

export async function getWorkouts(username: string = "") {
    let request_url = "";
    if (username === "") {
        request_url = `http://13.56.207.97:5000/workouts`;
    }
    else {
        request_url = `http://13.56.207.97:5000/workouts?username=${username}`;
    }
    const response = await fetch(request_url);
    const workouts: WorkoutsDTO[] = await response.json();
    return workouts;
};