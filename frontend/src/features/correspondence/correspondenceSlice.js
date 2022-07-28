import React from 'react';
import { createAsyncThunk, createEntityAdapter, createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

const correspondenceAdapter = createEntityAdapter()

const initialState = correspondenceAdapter.getInitialState({
  status: 'idle',
  error: null
})

export const fetchCorrespondence = createAsyncThunk('correspondence/fetchCorrespondence', async() => {
  const response = await axios.get('correspondence')
  return response.data
})

export const addNewCorrespondence = createAsyncThunk(
  'correspondence/addNewCorrespondece',
  async(initialCorrespondence) => {
    const response = await axios.post('correspondence', initialCorrespondence)
    return response.data
  }
)
const correspondenceSlice = createSlice({
  name: 'correspondence',
  initialState,
  reducers: {
    correspondecAdded(state,action){
      
    }
  },
  extraReducers(builder){
    builder
      .addCase(fetchCorrespondence.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(fetchCorrespondence.fulfilled, (state, action) => {
        state.status = 'succeeded'
        correspondenceAdapter.upsertMany(state, action.payload)
      })
      .addCase(fetchCorrespondence.rejected, (state, action) => {
        state.status = 'failed'
        state.error = action.error.message
      })
      .addCase(addNewCorrespondence.fulfilled, correspondenceAdapter.addOne)
  },
})

export const { correspondecAdded, } = correspondenceSlice.actions
export default correspondenceSlice.reducer
