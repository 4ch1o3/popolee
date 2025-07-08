import UploadIcon from "../assets/UploadButton.svg";

export const BottomBar = () => {
  return (
    <div className=" absolute bottom-0 left-0 w-full flex justify-center h-23">
      <div className=" bg-secondary w-fit p-1.5 rounded-full absolute bottom-13">
        <img src={UploadIcon} className="inline-block align-middle"></img>
      </div>
    </div>
  );
};
