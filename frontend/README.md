# these are the backend dependencies to install to the backend folder:
 "packages": {
    "": {
      "name": "backend",
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "cors": "^2.8.5",
        "csv-parser": "^3.0.0",
        "dotenv": "^16.3.1",
        "express": "^4.18.2",
        "fs": "^0.0.1-security",
        "mysql2": "^3.6.5",
        "sequelize": "^6.35.1"
      }
    },}

# these are the frontend dependencies to install in the frontend folder: 

"packages": {
    "": {
      "name": "frontend",
      "version": "0.1.0",
      "dependencies": {
        "@testing-library/jest-dom": "^5.17.0",
        "@testing-library/react": "^13.4.0",
        "@testing-library/user-event": "^13.5.0",
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "react-scripts": "5.0.1",
        "web-vitals": "^2.1.4"
      },
      "devDependencies": {
        "bootstrap": "^5.3.2",
        "concurrently": "^8.2.2",
        "react-bootstrap": "^2.9.1"
      }
    },
    
    }

# after all the packages are install with their appropriate folders
# cd into the frontend folder ./yelp_filtering/frontend:

npm start