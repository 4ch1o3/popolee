import { BottomBar } from "../components/bottom_bar";
import { TopBar } from "../components/top_bar";
import { FullProfile } from "../components/user_profile";

export const UserPage = () => {
  return (
    <div className="flex flex-col gap-3">
      <TopBar showSearch={true} showProfile={false} />
      <FullProfile />
      <BottomBar />
    </div>
  );
};
