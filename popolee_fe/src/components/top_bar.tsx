import { SmallLogo } from "./popolee_logo";

import Search from "../assets/icons/Search.svg";
import { UserProfile } from "./user_profile";

// const colorVariant = {
//   0: "img-placeholder-green",
//   1: "img-placeholder-blue",
//   2: "img-placeholder-pink",
//   3: "img-placeholder-purple",
//   4: "img-placeholder-orange",
//   5: "img-placeholder-yellow",
// };

const SearchIcon = () => {
  return (
    <a href="../search_user">
      <img
        src={Search}
        className="w-6 h-6 opacity-25 inline-block align-middle"
      ></img>
    </a>
  );
};

export const TopBar = ({
  showSearch,
  showProfile,
}: {
  showSearch: boolean;
  showProfile: boolean;
}) => {
  return (
    <div className="block">
      <div className="flex w-full min-h-8 justify-between items-center shrink-0">
        <SmallLogo />
        {showSearch && showProfile ? (
          <div className="flex w-fit gap-6 items-center">
            <SearchIcon />
            {/*
          TODO: isLoggedIn ? {isMyPage ? "로그아웃" : <UserProfile/>} : "로그인"
          */}
            <UserProfile />
          </div>
        ) : (
          <></>
        )}
      </div>
      <div></div>
    </div>
  );
};
