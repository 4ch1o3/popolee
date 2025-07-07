import UploadIcon from "../assets/icons/Upload.svg";

export const BottomBar = () => {
  return (
    <div className="absolute bottom-0 left-0 w-full flex justify-center h-23">
      <div className=" bg-secondary w-fit p-1.5 rounded-full absolute bottom-13">
        <div className="bg-primary w-fit p-4 rounded-full">
          <img
            src={UploadIcon}
            className="w-5.5 h-5.5 inline-block align-middle"
          ></img>
        </div>
      </div>
    </div>
  );
};
