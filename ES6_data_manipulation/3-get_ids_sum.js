export default function getStudentIdsSum(stutentids) {
    return stutentids.reduce((sum, stutentids) => sum + stutentids.id, 0);
  }
  