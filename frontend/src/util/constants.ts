import { WorkoutsDTO, WorkoutsGETParametersDTO } from "../dto/workouts.dto";

export const DEFAULT_WORKOUTS_GET_PARAMETERS: WorkoutsGETParametersDTO = {
    username: "user1",
    exercise: "",
    created_at: ""
};

export const DEFAULT_WORKOUTS: WorkoutsDTO[] = [{
    id: 0,
    username: "user1",
    exercise: "bicep curls",
    reps: 12,
    weight: 40,
    duration: 45,
    created_at: "2023-02-04T16:38:17.000Z",
    updated_at: "2023-02-04T16:38:17.000Z"
}];