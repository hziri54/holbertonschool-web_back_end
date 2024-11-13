import { ESLint } from 'eslint';

/** @type {import('eslint').Linter.Config} */
export default {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    // Ajoute d'autres configurations d'extension ici si nécessaire, comme 'plugin:react/recommended'
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  rules: {
    // Ajoute des règles personnalisées ici si nécessaire
  },
};
