// userController.ts
import { Request, Response } from "express";
import UserService from "../services/userService";
import { getUsersHandler } from "../handlers/getUserHandler";
import { createUserHandler } from "../handlers/createUserHandler";
import { editUserHandler } from "../handlers/editUserHandler";
import { deleteUserHandler } from "../handlers/deleteHandler";
import { getUserByIdHandler } from "../handlers/getUserByIdHandler";

class UserController {
	static createUser: any;
	static getUser: any;

	constructor(private userService: UserService) {}

	createUser = async (req: Request, res: Response): Promise<void> => {
		await createUserHandler(req, res);
	};

	getUsers = async (req: Request, res: Response): Promise<void> => {
		await getUsersHandler(req, res);
	};

	getUserById = async (req: Request, res: Response): Promise<void> => {
		await getUserByIdHandler(req, res);
	};

	editUser = async (req: Request, res: Response): Promise<void> => {
		await editUserHandler(req, res);
	};

	deleteUser = async (req: Request, res: Response): Promise<void> => {
		await deleteUserHandler(req, res);
	};
}

export default UserController;
