import { useProjects } from "../hooks/useProjects";

interface Props {
  value: string | null;
  onChange: (value: string | null) => void;
}

export function ProjectSelect({ value, onChange }: Props) {
  const { projects } = useProjects();

  return (
    <select
      className="select"
      value={value ?? ""}
      onChange={(event) => onChange(event.target.value || null)}
    >
      <option value="">No project</option>
      {projects.map((project) => (
        <option key={project.id} value={project.name}>
          {project.name}
        </option>
      ))}
    </select>
  );
}
