// import signInBackground from "../assets/signin_bg.png";
import { InputForm } from "../components/input_form";
import { LargeLogo } from "../components/popolee_logo";
export const SignIn = () => {
  return (
    <>
      <LargeLogo />
      <div className="w-full h-full overflow-clip justify-center">
        <InputForm placeholder={"이메일"} />
        <InputForm placeholder={"비밀번호"} />
      </div>
    </>
  );
};
