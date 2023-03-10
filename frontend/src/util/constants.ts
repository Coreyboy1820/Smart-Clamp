import { WorkoutsDTO, WorkoutsGETParametersDTO } from "../dto/workouts.dto";

export const CURRENT_USER = "user1";


export const WORKOUT_FILTERS: WorkoutsGETParametersDTO = {
    username: CURRENT_USER,
    exercise: "",
    created_at: new Date().toISOString().split('T')[0],
};

export const DEFAULT_WORKOUTS: WorkoutsDTO[] = [{
    id: 0,
    username: CURRENT_USER,
    exercise: "bicep curls",
    reps: 12,
    weight: 40,
    duration: 45,
    created_at: "2023-02-04T16:38:17.000Z",
    updated_at: "2023-02-04T16:38:17.000Z"
}];
