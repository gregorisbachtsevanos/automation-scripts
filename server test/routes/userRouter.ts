import { Router } from "express";
import userController from "../controllers/userController";

const router = Router();

router.get("/user/:userId", userController.getUser);
router.post("/user", userController.createUser);

export { router as userRouter };
