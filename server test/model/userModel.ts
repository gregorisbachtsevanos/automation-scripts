import { Schema, model, Document } from "mongoose";

interface IUser extends Document {
	name: string;
	email: string;
	// Add any other fields you need for your user model
}

const UserSchema = new Schema<IUser>({
	name: {
		type: String,
		required: true,
	},
	email: {
		type: String,
		required: true,
		unique: true,
	},
	// Add any other fields with their schema configurations
});

const userModel = model<IUser>("User", UserSchema);

export default userModel;
export { IUser };
