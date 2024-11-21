export default [
    {
      ignores: ['node_modules/**'],
    },
    {
      files: ['**/*.js'],
      languageOptions: {
        ecmaVersion: '2020',
        sourceType: 'module',
      },
      rules: {
        'indent': ['error', 2],
        'quotes': ['error', 'single'],
        'semi': ['error', 'always'],
        'no-trailing-spaces': 'error',
        'eol-last': ['error', 'always'],
      },
    },
  ];
  