{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a5e8f41e-099a-47b3-a966-74a68e345051",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in c:\\users\\windows 11\\anaconda3\\lib\\site-packages (1.26.4)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install numpy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "687571b4-cb65-431c-a85c-643608213c7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bd0c6a68-9bdd-4999-a06b-4fb7b49cb49f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1 = np.array([1,2,3,4,5,6,7,8,9,10])\n",
    "arr1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4abe9840-a10c-428c-b347-149dc07ab43c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4,  5],\n",
       "       [ 6,  7,  8,  9, 10]])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1.reshape(2,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1103e972-cffb-42d4-a4cc-06f6ad0d501f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])\n",
    "arr2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "accda43a-8dbe-408f-a4c0-2c3044179679",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2[5:15]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e8dfd527-ddb0-4415-a86b-4e376615c157",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\windows 11\\anaconda3\\lib\\site-packages (2.2.2)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\windows 11\\anaconda3\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\windows 11\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\windows 11\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\windows 11\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\windows 11\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9f950f64-f8da-472e-adf6-c5cfde9ea41e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Oranges    1\n",
       "Bananas    2\n",
       "Apples     3\n",
       "dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "ser1 = pd. Series ([1,2,3],index = [\"Oranges\",\"Bananas\",\"Apples\"])\n",
    "ser1\n",
    "                          "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "24854b6c-388d-4c5f-b297-9dc4510019dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Oranges    1\n",
       "Bananas    2\n",
       "Apples     3\n",
       "pears      4\n",
       "dtype: object"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ser1[\"pears\"] = 4\n",
    "ser1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "a28bd2cf-5e00-4661-8797-a6620a961b63",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mathew</td>\n",
       "      <td>34</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Diphu</td>\n",
       "      <td>32</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mary</td>\n",
       "      <td>35</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Abhirami</td>\n",
       "      <td>24</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Vishnu</td>\n",
       "      <td>26</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Abhul</td>\n",
       "      <td>27</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Nishad</td>\n",
       "      <td>31</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Christy</td>\n",
       "      <td>30</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Megha</td>\n",
       "      <td>20</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Ashiq</td>\n",
       "      <td>23</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Age  Gender\n",
       "1     Mathew   34    Male\n",
       "2      Diphu   32    Male\n",
       "3       Mary   35  Female\n",
       "4   Abhirami   24  Female\n",
       "5     Vishnu   26    Male\n",
       "6      Abhul   27    Male\n",
       "7     Nishad   31    Male\n",
       "8    Christy   30  Female\n",
       "9      Megha   20  Female\n",
       "10     Ashiq   23    Male"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ser2 = pd.DataFrame({'Name':[\"Mathew\",\"Diphu\",\"Mary\",\"Abhirami\",\"Vishnu\",\"Abhul\",\"Nishad\",\"Christy\",\"Megha\",\"Ashiq\"],'Age':\n",
    "                               [34,32,35,24,26,27,31,30,20,23], 'Gender':\n",
    "                               [\"Male\",\"Male\",\"Female\",\"Female\",\"Male\",\"Male\",\"Male\",\"Female\",\"Female\",\"Male\"]}, index = [1,2,3,4,5,6,7,8,9,10], \n",
    "                    columns = ['Name','Age','Gender'])\n",
    "ser2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "eabfde39-7c3e-4bc6-af42-0ad301274ab2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Occupation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mathew</td>\n",
       "      <td>34</td>\n",
       "      <td>Male</td>\n",
       "      <td>Programmer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Diphu</td>\n",
       "      <td>32</td>\n",
       "      <td>Male</td>\n",
       "      <td>programmer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mary</td>\n",
       "      <td>35</td>\n",
       "      <td>Female</td>\n",
       "      <td>Analyst</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Abhirami</td>\n",
       "      <td>24</td>\n",
       "      <td>Female</td>\n",
       "      <td>Manager</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Vishnu</td>\n",
       "      <td>26</td>\n",
       "      <td>Male</td>\n",
       "      <td>Analyst</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Abhul</td>\n",
       "      <td>27</td>\n",
       "      <td>Male</td>\n",
       "      <td>Programmer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Nishad</td>\n",
       "      <td>31</td>\n",
       "      <td>Male</td>\n",
       "      <td>Analyst</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Christy</td>\n",
       "      <td>30</td>\n",
       "      <td>Female</td>\n",
       "      <td>manager</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Megha</td>\n",
       "      <td>20</td>\n",
       "      <td>Female</td>\n",
       "      <td>Programmer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Ashiq</td>\n",
       "      <td>23</td>\n",
       "      <td>Male</td>\n",
       "      <td>Analsyt</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Age  Gender  Occupation\n",
       "1     Mathew   34    Male  Programmer\n",
       "2      Diphu   32    Male  programmer\n",
       "3       Mary   35  Female     Analyst\n",
       "4   Abhirami   24  Female     Manager\n",
       "5     Vishnu   26    Male     Analyst\n",
       "6      Abhul   27    Male  Programmer\n",
       "7     Nishad   31    Male     Analyst\n",
       "8    Christy   30  Female     manager\n",
       "9      Megha   20  Female  Programmer\n",
       "10     Ashiq   23    Male     Analsyt"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ser2[\"Occupation\"] = [\"Programmer\",\"programmer\",\"Analyst\",\"Manager\",\"Analyst\",\"Programmer\",\"Analyst\",\"manager\",\"Programmer\",\"Analsyt\"]\n",
    "ser2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "d49a994f-9b26-4dc4-9477-299ddb231783",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1      True\n",
       "2      True\n",
       "3      True\n",
       "4     False\n",
       "5     False\n",
       "6     False\n",
       "7      True\n",
       "8     False\n",
       "9     False\n",
       "10    False\n",
       "Name: Age, dtype: bool"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ser2[\"Age\"] > 30"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "5212b826-9bd7-413b-8493-920b3ed61b3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "ser2.to_csv('Python assignment 7.csv')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
