  export default function getListStudentIds(array) {
    if (!Array.isArray(list)) {
      return [];
    }
    return array.map((student) => student.id);
  }
