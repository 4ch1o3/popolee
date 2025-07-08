import PersonIcon from "../assets/icons/Person.svg?react";
import SortIcon from "../assets/icons/Sort.svg?react";
import TagIcon from "../assets/icons/Tag.svg?react";
import { chipType } from "./filter_list";

const iconMap: Record<chipType, React.FC<React.SVGProps<SVGSVGElement>>> = {
  Person: PersonIcon,
  Sort: SortIcon,
  Tag: TagIcon,
};

export const Chip = ({
  label,
  showIcon,
  type,
  onClick,
  isSelected,
}: {
  label: string;
  showIcon: boolean;
  type: chipType;
  onClick: React.MouseEventHandler<HTMLDivElement>;
  isSelected: boolean;
}) => {
  const Icon = iconMap[type];

  const iconColorClass = isSelected ? "text-secondary" : "text-primary";
  const chipColorClass = isSelected
    ? "bg-primary border-secondary text-secondary"
    : "bg-secondary border-primary text-primary";

  return (
    <div
      className={`${chipColorClass} rounded-full border-1 label w-fit px-3 py-2 gap-1.5 flex items-center text-center shrink-0`}
      onClick={onClick}
    >
      {showIcon && iconMap[type] ? (
        <Icon className={`w-3 h-3 fill-current ${iconColorClass}`}></Icon>
      ) : (
        <></>
      )}
      {label}
    </div>
  );
};
