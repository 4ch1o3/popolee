import Person from "../assets/icons/Person.svg";
import Sort from "../assets/icons/Sort.svg";
import Tag from "../assets/icons/Tag.svg";

type chipType = "Person" | "Sort" | "Tag";

const iconMap: Record<chipType, string> = {
  Person,
  Sort,
  Tag,
};

export const Chip = ({
  label,
  showIcon,
  type,
  onClick,
}: {
  label: string;
  showIcon: boolean;
  type: chipType;
  onClick: React.MouseEventHandler<HTMLDivElement>;
}) => {
  return (
    <div
      className={`rounded-full border-1 label w-fit px-3 py-2 gap-1.5 flex items-center shrink-0`}
      onClick={onClick}
    >
      {showIcon && iconMap[type] ? (
        <img src={iconMap[type]} className="h-3"></img>
      ) : (
        <></>
      )}
      {label}
    </div>
  );
};
