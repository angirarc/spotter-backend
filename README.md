# Spotter Django Backend

## Vercel Deployment Instructions

### Prerequisites

1. A Vercel account
2. PostgreSQL database (you can use Vercel Postgres, Supabase, or any other PostgreSQL provider)

### Deployment Steps

1. **Install Vercel CLI**
   ```
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```
   vercel login
   ```

3. **Deploy to Vercel**
   Navigate to the project directory and run:
   ```
   vercel
   ```

4. **Set Environment Variables**
   After deploying, set up the following environment variables in the Vercel dashboard:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: Set to 'False' for production
   - `DATABASE_URL`: Your PostgreSQL connection string

### Database Configuration

1. Create a PostgreSQL database with your preferred provider
2. Get the connection string in the format: `postgresql://username:password@host:port/database`
3. Add this as the `DATABASE_URL` environment variable in Vercel

### Important Notes

- The application is configured to use `settings_vercel.py` when deployed to Vercel
- Static files are configured to be collected in the `staticfiles` directory
- Make sure your database is accessible from Vercel's servers

### Local Development

1. Create a `.env` file based on `.env.example`
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`

### Project Structure

- `vercel.json`: Configuration for Vercel deployment
- `build_files.sh`: Script that runs during build process
- `requirements.txt`: Python dependencies
- `runtime.txt`: Python version specification
- `spotter/settings_vercel.py`: Settings file used in Vercel environment