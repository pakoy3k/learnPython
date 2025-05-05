{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec1c4f02-558d-4781-8dcd-c3f69a1a2e2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_sustantivos(palabra):\n",
    "    fid = open('db.txt')\n",
    "    for line in fid:\n",
    "        data = line.split(':')#0-> token, 1->lista palabras        \n",
    "        #print(f\"\\n\\t DEBUG: {data[1]} \\t {palabra}\")\n",
    "        #print(f\"encontrado {data[0]}\") if palabra in data[1] else print(\"\")    \n",
    "        for db_string in data[1].split(','):\n",
    "            #print(f\"busca [{db_string} -> [{palabra}]\")\n",
    "            if palabra in db_string:\n",
    "                print(f\"\\n\\t Si lo encontre y su token es {data[0]}\\n\")\n",
    "                fid.close()\n",
    "                return data[0]\n",
    "    \n",
    "    fid.close()"
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
