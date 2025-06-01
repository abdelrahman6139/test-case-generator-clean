import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Homepage, login, and register', () => {
  render(<App />);
  expect(screen.getByText(/Welcome to the Homepage/i)).toBeInTheDocument();
  expect(screen.getByText(/Login Page/i)).toBeInTheDocument();
  expect(screen.getByText(/Register Page/i)).toBeInTheDocument();
});