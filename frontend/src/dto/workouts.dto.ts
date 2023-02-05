export interface WorkoutsDTO {
    id: number;
    username: string;
    exercise: string;
    reps: number;
    weight: number;
    duration: number;
    created_at: string;
    updated_at: string;
}

export interface WorkoutsGETParametersDTO {
    username: string;
    exercise: string;
    created_at: string;
}
