import signUpUser from './4-all-reject';
import uploadPhoto from './5-all-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const proms = [
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ];
  const a = Promise.resolve(await Promise.allSettled(proms));
  return a;
}
