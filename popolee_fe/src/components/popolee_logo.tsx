import logoSmall from "../assets/logo-small.svg";
import logoMedium from "../assets/logo-medium.svg";
import logoLarge from "../assets/logo-large.svg";

export const SmallLogo = () => {
  return (
    <div className="mt-2 inline-block align-middle">
      <a href="../">
        <img src={logoSmall}></img>
      </a>
    </div>
  );
};

export const MediumLogo = () => {
  return (
    <div>
      <a href="../">
        <img src={logoMedium}></img>
      </a>
    </div>
  );
};

export const LargeLogo = () => {
  return (
    <div>
      <a href="../">
        <img src={logoLarge}></img>
      </a>
    </div>
  );
};
